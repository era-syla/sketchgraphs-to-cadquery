import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0345, 0.0525).lineTo(-0.0155, 0.0525).threePointArc((-0.01338, 0.05162), (-0.0125, 0.0495)).lineTo(-0.0125, 0.0305).threePointArc((-0.01338, 0.02838), (-0.0155, 0.0275)).lineTo(-0.0345, 0.0275).threePointArc((-0.03662, 0.02838), (-0.0375, 0.0305)).lineTo(-0.0375, 0.0495).threePointArc((-0.03662, 0.05162), (-0.0345, 0.0525)).close()
solid=wp_sketch0.add(loop0).extrude(-0.014336369345210577)
