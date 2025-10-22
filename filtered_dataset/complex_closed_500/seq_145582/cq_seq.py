import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 0.0762).threePointArc((0.0381, 0.1143), (0.0762, 0.0762)).lineTo(0.0762, 0.0).threePointArc((0.0381, -0.0381), (0.0, -0.0)).close()
solid=wp_sketch0.add(loop0).extrude(0.0027255956771162267)
