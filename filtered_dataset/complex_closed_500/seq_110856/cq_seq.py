import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.24, 0.99077).threePointArc((0.12089, 1.01267), (0.0, 1.02)).lineTo(0.0, 0.95).lineTo(0.283, 0.95).threePointArc((0.26688, 0.97607), (0.24, 0.99077)).close()
solid=wp_sketch0.add(loop0).extrude(-0.7665539841219065)
