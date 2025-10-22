import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.03274, 0.01594).lineTo(0.03956, 0.01594).threePointArc((0.04405, 0.01408), (0.04591, 0.00959)).lineTo(0.04591, -0.00771).threePointArc((0.04405, -0.0122), (0.03956, -0.01406)).lineTo(-0.03274, -0.01406).threePointArc((-0.03723, -0.0122), (-0.03909, -0.00771)).lineTo(-0.03909, 0.00959).threePointArc((-0.03723, 0.01408), (-0.03274, 0.01594)).close()
solid=wp_sketch0.add(loop0).extrude(-0.0011278964873768025)
