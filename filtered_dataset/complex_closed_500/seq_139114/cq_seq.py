import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.02476, 0.0146).lineTo(0.02477, 0.0146).threePointArc((0.02746, 0.01349), (0.02858, 0.01079)).lineTo(0.02857, -0.01079).threePointArc((0.02746, -0.01349), (0.02476, -0.0146)).lineTo(-0.02477, -0.0146).threePointArc((-0.02746, -0.01349), (-0.02858, -0.01079)).lineTo(-0.02857, 0.01079).threePointArc((-0.02746, 0.01349), (-0.02476, 0.0146)).close()
solid=wp_sketch0.add(loop0).extrude(-0.06737871625758635)
