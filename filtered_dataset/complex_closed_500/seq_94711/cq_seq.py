import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.05492, 0.01591).threePointArc((-0.05543, 0.01205), (-0.05425, 0.00833)).threePointArc((-0.04841, 0.00405), (-0.0413, 0.00546)).threePointArc((-0.03909, 0.00767), (-0.03777, 0.01051)).threePointArc((-0.03777, 0.01519), (-0.04013, 0.01923)).threePointArc((-0.04843, 0.02162), (-0.05492, 0.01591)).close()
solid=wp_sketch0.add(loop0).extrude(-0.01352795236015281)
