import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.03701, 0.04403).lineTo(-0.06876, 0.04403).threePointArc((-0.07101, 0.04496), (-0.07194, 0.04721)).lineTo(-0.07194, 0.06308).threePointArc((-0.07101, 0.06533), (-0.06876, 0.06626)).lineTo(-0.03701, 0.06626).threePointArc((-0.03477, 0.06533), (-0.03384, 0.06308)).lineTo(-0.03384, 0.04721).threePointArc((-0.03477, 0.04496), (-0.03701, 0.04403)).close()
solid=wp_sketch0.add(loop0).extrude(0.0017677143706921969)
