import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.01, 0.02398).lineTo(-0.01, 0.02398).lineTo(-0.01, 0.02598).lineTo(0.01, 0.02598).lineTo(0.01, 0.02398).close()
solid=wp_sketch0.add(loop0).extrude(-0.034794111118341256)
