# Dev-Soft-Parcial2

* Luis Miguel Lasso Mesa 
* ID: 408327
* Tecnología en desarrollo de software
* Diseño: Para el desarrollo de esta API se optó por Python con FastAPI debido a su simplicidad, alto rendimiento y soporte nativo para tipado y documentación automática mediante OpenAPI. Se siguió un enfoque de arquitectura limpia, separando claramente las responsabilidades en módulos: controller para la definición de endpoints, service para la lógica de negocio, repository para el acceso a datos, model para las entidades de dominio y dto para la transferencia de datos.
  Esta separación busca garantizar un código mantenible, escalable y fácil de probar. Los controladores no contienen lógica de negocio ni acceden directamente a los datos, sino que delegan   toda la funcionalidad al servicio, que a su vez interactúa con el repositorio. Esta decisión permite cambiar la fuente de datos (por ejemplo, de memoria a una base de datos real) sin modificar la capa de presentación ni la lógica principal, cumpliendo así con los principios de inversión de dependencias y separación de responsabilidades.
* Video: 
