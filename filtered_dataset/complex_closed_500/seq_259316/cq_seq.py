import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0, 0.04445).threePointArc((-0.04445, -0.0), (-0.0, -0.04445)).lineTo(0.0762, -0.04445).threePointArc((0.12065, -0.0), (0.0762, 0.04445)).lineTo(0.0, 0.04445).close()
solid=wp_sketch0.add(loop0).extrude(0.20605683974379918)
