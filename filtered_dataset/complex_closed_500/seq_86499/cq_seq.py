import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00467, 0.00761).lineTo(0.0251, 0.00761).lineTo(0.0251, -0.02596).lineTo(-0.00467, -0.02596).lineTo(-0.00467, 0.00761).close()
solid=wp_sketch0.add(loop0).extrude(0.07197505907541608)
