import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01701, -0.02888).lineTo(-0.01644, -0.02888).lineTo(-0.01644, 0.02881).lineTo(0.0169, 0.02881).lineTo(0.01701, -0.02888).close()
solid=wp_sketch0.add(loop0).extrude(0.1535263473215944)
