import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0368).lineTo(0.257, 0.0368).lineTo(0.257, 0.0568).lineTo(0.0, 0.0568).lineTo(0.0, 0.0368).close()
solid=wp_sketch0.add(loop0).extrude(-0.015243107152163916)
