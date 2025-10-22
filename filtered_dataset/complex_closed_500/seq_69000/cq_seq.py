import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.05603, 0.00626).lineTo(0.04953, 0.00626).lineTo(0.04953, 0.0125).lineTo(0.05603, 0.0125).lineTo(0.05603, 0.00626).close()
solid=wp_sketch0.add(loop0).extrude(0.0131840038849661)
