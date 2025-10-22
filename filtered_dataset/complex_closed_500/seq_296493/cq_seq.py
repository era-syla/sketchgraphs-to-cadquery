import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0045, 0.159).lineTo(0.017, 0.159).lineTo(0.017, 0.1365).lineTo(0.0045, 0.1365).lineTo(0.0045, 0.159).close()
solid=wp_sketch0.add(loop0).extrude(0.04659850802795882)
