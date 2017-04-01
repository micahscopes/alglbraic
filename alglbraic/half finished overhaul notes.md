* VectorSpace has no norm by default, use Norm for that.
* size constants are now the preferred way to "namespace" functions/fragments, since glsl is statically typed.
  - give fragments a consistent way to link into these "namespaces"
  - is it necessary to name functions differently?  i.e. rotateM vs rotateN, rather than relying on their return type being float[N] vs float[M]
* RotationOperation
* Consolidate the mul, mul3, etc. helpers that rely on the "product" operation.  Maybe overhaul the VectorOperation class with convenience functions for repeated application, etc.