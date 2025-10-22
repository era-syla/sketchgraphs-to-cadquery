import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.04807, 0.04273).lineTo(0.06254, 0.04273).lineTo(0.06254, -0.06127).lineTo(-0.04807, -0.06127).lineTo(-0.04807, 0.04273).close()
solid=wp_sketch0.add(loop0).extrude(-0.14399498083707302)
