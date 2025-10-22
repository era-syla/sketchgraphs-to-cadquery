import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.28164, -0.09808).lineTo(-0.28164, -0.22508).lineTo(-0.30858, -0.25202).lineTo(-0.33552, -0.22508).lineTo(-0.33552, -0.09808).lineTo(-0.30858, -0.07114).lineTo(-0.28164, -0.09808).close()
solid=wp_sketch0.add(loop0).extrude(-0.2707866974841719)
