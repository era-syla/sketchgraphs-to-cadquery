import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00801, 0.01862).lineTo(0.07354, 0.0).lineTo(0.00801, 0.0).lineTo(0.00801, 0.01862).close()
solid=wp_sketch0.add(loop0).extrude(-0.10789408692242115)
