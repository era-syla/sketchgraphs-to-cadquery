import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00243, 0.00391).threePointArc((0.00224, 0.0041), (0.00199, 0.00416)).lineTo(0.00034, 0.00416).threePointArc((9e-05, 0.0041), (-0.0001, 0.00391)).lineTo(-0.00067, 0.00291).lineTo(-0.0001, 0.00291).lineTo(0.00243, 0.00291).lineTo(0.00243, 0.00391).close()
solid=wp_sketch0.add(loop0).extrude(-0.0009722573005848011)
