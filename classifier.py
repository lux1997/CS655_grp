from torchvision.models import resnet101
from torchvision import transforms
from torch.autograd import Variable
from PIL import Image

class Classifier():
    def __init__(self):
        # load pretrained model
        self.model = resnet101(pretrained=True)
        self.model.eval()
        # image preprocessing
        self.transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                std=[0.229, 0.224, 0.225]),
        ])
        # Load id-to-classname files
        with open('data/imagenet_synsets.txt', 'r') as f:
            synsets = f.readlines()
        synsets = [x.strip() for x in synsets]
        splits = [line.split(' ') for line in synsets]
        self.key_to_classname = {spl[0]:' '.join(spl[1:]) for spl in splits}
        with open('data/imagenet_classes.txt', 'r') as f:
            class_id_to_key = f.readlines()
        self.class_id_to_key = [x.strip() for x in class_id_to_key]
    
    def predict(self, img):
        # image preprocessing
        img = self.transform(img)
        # predict
        output = self.model(Variable(img.unsqueeze(0)))
        # get class id
        _, argmax = output.data.squeeze().max(0)
        # convert class id to class name
        class_key = self.class_id_to_key[argmax]
        classname = self.key_to_classname[class_key]
        return classname

if __name__ == '__main__':
    classifier = Classifier()
    img = Image.open("data/dog.jpg")
    print(classifier.predict(img))
