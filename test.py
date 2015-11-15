from openalpr import Alpr
import sys

alpr = Alpr("eu", "nplate_train/openalpr.conf.in", "nplate_train/runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)

#alpr.set_top_n(20)
alpr.set_default_region("eu")

results = alpr.recognize_file("/home/riaz/Desktop/hack/2009_09_08_drive_0010/I1_000388.png")

for plate in results['results']:

    if len(plate['candidates']) > 0:
        print "Found: %12s %12f" % ( plate['candidates'][0]['plate'],plate['candidates'][0]['confidence']) 
        
# Call when completely done to release memory
alpr.unload()
