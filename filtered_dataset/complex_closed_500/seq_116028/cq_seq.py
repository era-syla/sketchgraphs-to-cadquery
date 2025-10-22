import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0951, 0.00635).lineTo(-0.12733, 0.00635).lineTo(-0.12724, 0.05972).lineTo(-0.08318, 0.05972).lineTo(-0.08324, 0.0262).threePointArc((-0.09228, 0.01814), (-0.0951, 0.00635)).close()
solid=wp_sketch0.add(loop0).extrude(-0.08363622282616609)
