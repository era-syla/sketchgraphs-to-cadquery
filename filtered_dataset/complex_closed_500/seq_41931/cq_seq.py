import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.03556, 0.01778).lineTo(0.03556, 0.01778).lineTo(0.03556, -0.01778).lineTo(-0.03556, -0.01778).lineTo(-0.03556, 0.01778).close()
solid=wp_sketch0.add(loop0).extrude(-0.09035523628307146)
