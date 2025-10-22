import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.05, -0.0133).lineTo(-0.05, 0.0133).threePointArc((-0.04813, 0.01862), (-0.04334, 0.0216)).threePointArc((-0.0, 0.02635), (0.04334, 0.0216)).threePointArc((0.04813, 0.01862), (0.05, 0.0133)).lineTo(0.05, -0.0133).threePointArc((0.04813, -0.01862), (0.04334, -0.0216)).threePointArc((0.0, -0.02635), (-0.04334, -0.0216)).threePointArc((-0.04813, -0.01862), (-0.05, -0.0133)).close()
solid=wp_sketch0.add(loop0).extrude(0.10257388211352288)
