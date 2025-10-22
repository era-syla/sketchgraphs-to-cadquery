import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0605, 0.01325).lineTo(-0.0745, 0.01325).lineTo(-0.0745, 0.00725).lineTo(-0.0605, 0.00725).lineTo(-0.0605, 0.01325).close()
solid=wp_sketch0.add(loop0).extrude(-0.040332396149007715)
