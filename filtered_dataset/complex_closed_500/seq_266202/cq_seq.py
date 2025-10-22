import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.001, 0.0).lineTo(0.006, 0.0).lineTo(0.006, 0.02051).lineTo(0.01594, 0.02051).lineTo(0.01594, 0.0).lineTo(0.01794, 0.0).lineTo(0.021, 0.035).lineTo(0.019, 0.035).threePointArc((0.01317, 0.02792), (0.005, 0.02376)).lineTo(0.001, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.07643566566721592)
