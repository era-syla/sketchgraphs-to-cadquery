import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).threePointArc((0.00307, 0.04937), (-0.04008, 0.02519)).threePointArc((-0.00158, 0.04198), (0.0, 0.0)).close()
solid=wp_sketch0.add(loop0).extrude(-0.12862975071387786)
