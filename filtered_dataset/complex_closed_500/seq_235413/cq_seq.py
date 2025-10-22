import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.0165, 0.0175).lineTo(-0.00775, 0.0175).lineTo(-0.00775, 0.0125).lineTo(-0.0165, 0.0125).lineTo(-0.0165, 0.0175).close()
solid=wp_sketch0.add(loop0).extrude(0.012818378606675842)
