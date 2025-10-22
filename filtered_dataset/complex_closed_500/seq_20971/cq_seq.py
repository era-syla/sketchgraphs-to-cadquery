import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.4225, 0.0765).lineTo(-0.1425, 0.0765).lineTo(-0.1425, 0.4115).lineTo(0.4225, 0.4115).lineTo(0.4225, 0.0765).close()
solid=wp_sketch0.add(loop0).extrude(1.334259752212345)
