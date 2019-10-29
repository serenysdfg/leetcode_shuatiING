class Classifier{
	public:
		Classifier(const string &model_file,const string trained_file);
		int Classify(const cv::Mat& img);
	private:
		std::vector<int> Predict(const cv::Mat& img);
		void WrapInputLayer(std::vector<cv::Mat>* input_channels);  
		void Preprocess(const cv::Mat& img,   std::vector<cv::Mat>* input_channels);
		private:  
    shared_ptr<Net<float> > net_;  
    cv::Size input_geometry_;  
    int num_channels_;  
};  
  
Classifier::Classifier(const string& model_file,  
    const string& trained_file)   
{  
#ifdef CPU_ONLY  
    Caffe::set_mode(Caffe::CPU);  
#else  
    Caffe::set_mode(Caffe::GPU);  
#endif  
  
    /* Load the network. */  
    net_.reset(new Net<float>(model_file, TEST));  
    net_->CopyTrainedLayersFrom(trained_file);  
  
    CHECK_EQ(net_->num_inputs(), 1) << "Network should have exactly one input.";  
    CHECK_EQ(net_->num_outputs(), 1) << "Network should have exactly one output.";  
  
    Blob<float>* input_layer = net_->input_blobs()[0];  
    num_channels_ = input_layer->channels();  
    CHECK(num_channels_ == 3 || num_channels_ == 1)  
        << "Input layer should have 1 or 3 channels.";  
    input_geometry_ = cv::Size(input_layer->width(), input_layer->height());  
  
}  
  
/* Return the top N predictions. */  
int Classifier::Classify(const cv::Mat& img) {  
    std::vector<int> output = Predict(img);  
    std::vector<int>::iterator iter=find(output.begin(), output.end(), 1);  
    int prediction = distance(output.begin(), iter);  
    return prediction<10 ? prediction:0;  
}  
std::vector<int> Classifier::Predict(const cv::Mat& img) {  
    Blob<float>* input_layer = net_->input_blobs()[0];  
    input_layer->Reshape(1, num_channels_,  
        input_geometry_.height, input_geometry_.width);  
    /* Forward dimension change to all layers. */  
    net_->Reshape();  
  
    std::vector<cv::Mat> input_channels;  
    WrapInputLayer(&input_channels);  
  
    Preprocess(img, &input_channels);  
  
    net_->Forward();  
  
    /* Copy the output layer to a std::vector */  
    Blob<float>* output_layer = net_->output_blobs()[0];  
    const float* begin = output_layer->cpu_data();  
    const float* end = begin + output_layer->channels();  
    return std::vector<int>(begin, end);  
}  
  
void Classifier::WrapInputLayer(std::vector<cv::Mat>* input_channels) {  
    Blob<float>* input_layer = net_->input_blobs()[0];  
  
    int width = input_layer->width();  
    int height = input_layer->height();  
    float* input_data = input_layer->mutable_cpu_data();  
    for (int i = 0; i < input_layer->channels(); ++i) {  
        cv::Mat channel(height, width, CV_32FC1, input_data);  
        input_channels->push_back(channel);  
        input_data += width * height;  
    }  
}  
  
void Classifier::Preprocess(const cv::Mat& img,  
    std::vector<cv::Mat>* input_channels) {  
    /* Convert the input image to the input image format of the network. */  
    cv::Mat sample;  
    if (img.channels() == 3 && num_channels_ == 1)  
        cv::cvtColor(img, sample, cv::COLOR_BGR2GRAY);  
    else if (img.channels() == 4 && num_channels_ == 1)  
        cv::cvtColor(img, sample, cv::COLOR_BGRA2GRAY);  
    else if (img.channels() == 4 && num_channels_ == 3)  
        cv::cvtColor(img, sample, cv::COLOR_BGRA2BGR);  
    else if (img.channels() == 1 && num_channels_ == 3)  
        cv::cvtColor(img, sample, cv::COLOR_GRAY2BGR);  
    else  
        sample = img;  
  
    cv::Mat sample_resized;  
    if (sample.size() != input_geometry_)  
        cv::resize(sample, sample_resized, input_geometry_);  
    else  
        sample_resized = sample;  
  
    cv::Mat sample_float;  
    if (num_channels_ == 3)  
        sample_resized.convertTo(sample_float, CV_32FC3);  
    else  
        sample_resized.convertTo(sample_float, CV_32FC1);  
  
    cv::split(sample_float, *input_channels);  
  
    CHECK(reinterpret_cast<float*>(input_channels->at(0).data)  
        == net_->input_blobs()[0]->cpu_data())  
        << "Input channels are not wrapping the input layer of the network.";  
}  
  
  
static void on_Mouse(int event, int x, int y, int flags, void*)  
{  
  
  
  
    if (event == EVENT_LBUTTONUP || !(flags&EVENT_FLAG_LBUTTON))  
    {  
        previousPoint = Point(-1,-1);  
    }  
    else  
        if (event == EVENT_LBUTTONDOWN)  
        {  
            previousPoint = Point(x, y);  
        }  
        else if (event == EVENT_MOUSEMOVE || (flags&EVENT_FLAG_LBUTTON))  
        {  
            Point pt(x, y);  
            if (previousPoint.x<0)  
            {  
                previousPoint = pt;  
            }  
            line(srcimage, previousPoint, pt, Scalar(255), 16, 8, 0);  
            previousPoint = pt;  
            imshow("result", srcimage);  
        }  
  
}  
  
  
int main(int argc, char** argv)  
{  
  
    ::google::InitGoogleLogging(argv[0]);  
  
#ifdef CPU_ONLY  
    Caffe::set_mode(Caffe::CPU);  
#else  
    Caffe::set_mode(Caffe::GPU);  
#endif  
  
    string model_file = "lenet.prototxt";  
    string trained_file = "lenet_iter_10000.caffemodel";  
    Classifier classifier(model_file, trained_file);  
  
    std::cout << "------directed by watersink------" << std::endl;  
    std::cout << "------------enter:退出-----------" << std::endl;  
    std::cout << "--------------1:还原-------------" << std::endl;  
    std::cout << "-------------2:写数字------------" << std::endl;  
    std::cout << "-----watersink2016@gmail.com-----" << std::endl;  
  
  
    imshow("result", srcimage);  
    setMouseCallback("result", on_Mouse, 0);  
    while (1)  
    {  
        char c = (char)waitKey();  
        if (c == 27)  
            break;  
        if (c=='1')  
        {  
            srcimageori.copyTo(srcimage);  
            imshow("result", srcimage);  
        }  
        if (c == '2')  
        {  
            cv::Mat img;  
            cv::resize(srcimage, img, cv::Size(28, 28));  
            CHECK(!img.empty()) << "Unable to decode image " << std::endl;  
            int  prediction = classifier.Classify(img);  
            std::cout << "prediction:" << prediction << std::endl;  
            imshow("result", srcimage);  
        }  
    }  
  
      
    waitKey();  
    return 0;  
  
}  
};
