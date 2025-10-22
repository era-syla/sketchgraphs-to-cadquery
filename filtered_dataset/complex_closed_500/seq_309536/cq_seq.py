import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.24565, -0.23564).threePointArc((0.25363, -0.26114), (0.26162, -0.23564)).lineTo(0.24565, -0.23564).close()
solid=wp_sketch0.add(loop0).extrude(-0.016988854450221694)
