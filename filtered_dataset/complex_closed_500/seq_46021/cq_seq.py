import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.1034, 0.02695).lineTo(0.09947, 0.02695).lineTo(0.09947, 0.03858).lineTo(0.1034, 0.03858).lineTo(0.1034, 0.02695).close()
solid=wp_sketch0.add(loop0).extrude(0.03376172058855176)
