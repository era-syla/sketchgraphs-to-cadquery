import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00285, 0.01718).lineTo(0.00285, 0.01718).lineTo(0.00285, 0.01458).lineTo(-0.00285, 0.01458).lineTo(-0.00285, 0.01718).close()
solid=wp_sketch0.add(loop0).extrude(0.013240239402861943)
