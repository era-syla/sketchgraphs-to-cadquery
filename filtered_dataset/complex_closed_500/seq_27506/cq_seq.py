import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.6, -0.325).lineTo(-0.6, -0.325).lineTo(-0.6, 0.325).lineTo(0.6, 0.325).lineTo(0.6, -0.325).close()
solid=wp_sketch0.add(loop0).extrude(2.547991806747606)
