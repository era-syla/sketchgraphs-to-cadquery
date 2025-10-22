import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-1.60704, 0.08484).lineTo(0.09296, 0.08484).lineTo(0.09296, -0.01516).lineTo(-1.60704, -0.01516).lineTo(-1.60704, 0.08484).close()
solid=wp_sketch0.add(loop0).extrude(1.5558478791812673)
