import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0041).lineTo(0.00665, 0.0041).lineTo(0.00665, 0.0).lineTo(0.01, 0.0).lineTo(0.01, 0.01).lineTo(0.0, 0.01).lineTo(0.0, 0.0041).close()
solid=wp_sketch0.add(loop0).extrude(0.009044726597294469)
