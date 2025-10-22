import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0, -0.03596).threePointArc((0.03596, -0.0), (0.0, 0.03596)).lineTo(0.0, -0.03596).close()
solid=wp_sketch0.add(loop0).extrude(0.017330610505473087)
