import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0025, 0.0025).lineTo(0.6725, 0.0025).lineTo(0.6725, 1.0025).lineTo(0.0025, 1.0025).lineTo(0.0025, 0.0025).close()
solid=wp_sketch0.add(loop0).extrude(-2.4547177648276053)
