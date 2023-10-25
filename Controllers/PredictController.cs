
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.ML;
using Alexander_cuartas_emociones_parcial_2;
using System.IO;

namespace alexander_cuartas_emociones_parcial_2.Controllers
{
    [Route("api/predict")]
    [ApiController]
    public class PredictController : ControllerBase
    {

        [HttpPost]
        public JsonResult Post([FromForm] Image image)
        {
            var imageBytes = System.IO.File.ReadAllBytes(@"C:\Users\alextron\Documents\programming\patrones\alexander_cuartas_emociones_parcial_2\images\Alegre\1.jpeg");
            EmocionesML.ModelInput sampleData = new EmocionesML.ModelInput()
            {
                ImageSource = imageBytes,
            };

            //Load model and predict output
            var result = EmocionesML.Predict(sampleData);
            return new JsonResult(new Predict { Emotion = "Alegre" });
        }
    }
}


public class Image
{
    public string Name { get; set; }
    public IFormFile FormFile { get; set; }

}

