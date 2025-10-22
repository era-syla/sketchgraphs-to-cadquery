import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.1082, -0.05787).threePointArc((0.11054, -0.05404), (0.1067, -0.0517)).lineTo(0.10359, -0.05245).lineTo(0.10284, -0.04937).lineTo(0.10595, -0.04861).threePointArc((0.11362, -0.05329), (0.10895, -0.06096)).lineTo(0.10584, -0.06171).lineTo(0.10509, -0.05863).lineTo(0.1082, -0.05787).close()
solid=wp_sketch0.add(loop0).extrude(0.019583936320497028)
