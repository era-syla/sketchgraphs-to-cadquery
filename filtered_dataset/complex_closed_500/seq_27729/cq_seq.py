import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.1651, 0.1143).lineTo(-0.1651, 0.1143).lineTo(-0.1651, -0.1143).lineTo(0.1651, -0.1143).lineTo(0.1651, 0.1143).close()
solid=wp_sketch0.add(loop0).extrude(0.8216300954708896)
