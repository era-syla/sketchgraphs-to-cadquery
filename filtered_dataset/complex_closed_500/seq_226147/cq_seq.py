import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.02, -0.0095).lineTo(0.017, -0.0095).lineTo(0.017, -0.0065).lineTo(0.02, -0.0065).lineTo(0.02, -0.0095).close()
solid=wp_sketch0.add(loop0).extrude(0.0008005863037430725)
