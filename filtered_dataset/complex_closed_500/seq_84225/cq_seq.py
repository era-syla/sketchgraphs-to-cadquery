import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.21229, 0.38838).lineTo(0.06715, -0.01905).lineTo(0.2286, -0.01905).lineTo(0.2286, 0.38838).lineTo(0.21229, 0.38838).close()
solid=wp_sketch0.add(loop0).extrude(0.8733203307056849)
