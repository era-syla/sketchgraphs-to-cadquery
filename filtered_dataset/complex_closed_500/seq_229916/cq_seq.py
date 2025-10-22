import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.01905).lineTo(0.00318, 0.01905).threePointArc((0.00588, -0.01008), (0.00318, -0.03922)).lineTo(0.0, -0.03922).threePointArc((0.0023, -0.01008), (0.0, 0.01905)).close()
solid=wp_sketch0.add(loop0).extrude(0.11607917008193065)
