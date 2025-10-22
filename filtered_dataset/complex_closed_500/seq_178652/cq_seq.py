import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.009, 0.00313).threePointArc((-0.00953, 0.0), (0.009, -0.00313)).threePointArc((0.00635, 0.0), (0.009, 0.00313)).close()
solid=wp_sketch0.add(loop0).extrude(-0.04477295349731785)
