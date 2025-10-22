import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.06478, 0.19397).lineTo(-0.06214, 0.19397).threePointArc((-0.05861, 0.19251), (-0.05714, 0.18897)).lineTo(-0.05714, 0.17539).lineTo(-0.06478, 0.17539).lineTo(-0.06478, 0.19397).close()
solid=wp_sketch0.add(loop0).extrude(-0.039610884899719805)
