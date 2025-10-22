import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.07625, -0.07425).lineTo(-0.07625, -0.07425).threePointArc((-0.08191, -0.07191), (-0.08425, -0.06625)).lineTo(-0.08425, 0.06625).threePointArc((-0.08191, 0.07191), (-0.07625, 0.07425)).lineTo(0.07625, 0.07425).threePointArc((0.08191, 0.07191), (0.08425, 0.06625)).lineTo(0.08425, -0.06625).threePointArc((0.08191, -0.07191), (0.07625, -0.07425)).close()
solid=wp_sketch0.add(loop0).extrude(0.36280976416321675)
