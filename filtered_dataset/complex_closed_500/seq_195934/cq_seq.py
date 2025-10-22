import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0237, -0.0158).lineTo(-0.0237, -0.0158).lineTo(-0.0237, 0.0158).lineTo(0.0237, 0.0158).lineTo(0.0237, -0.0158).close()
solid=wp_sketch0.add(loop0).extrude(0.01606744631069697)
