import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.16828, 0.17463).lineTo(0.16828, 0.17463).lineTo(0.16828, -0.17463).lineTo(-0.16828, -0.17463).lineTo(-0.16828, 0.17463).close()
solid=wp_sketch0.add(loop0).extrude(-0.49463663496317367)
