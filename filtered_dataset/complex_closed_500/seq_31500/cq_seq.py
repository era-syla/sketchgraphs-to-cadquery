import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.212, 0.0095).lineTo(0.188, 0.0095).lineTo(0.188, -0.0205).lineTo(0.212, -0.0205).lineTo(0.212, 0.0095).close()
solid=wp_sketch0.add(loop0).extrude(-0.06879322769080674)
