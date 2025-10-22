import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0781, 0.04794).lineTo(0.07001, 0.04794).lineTo(0.07001, -0.07906).lineTo(-0.0781, -0.07906).lineTo(-0.0781, 0.04794).close()
solid=wp_sketch0.add(loop0).extrude(-0.3230568271049767)
