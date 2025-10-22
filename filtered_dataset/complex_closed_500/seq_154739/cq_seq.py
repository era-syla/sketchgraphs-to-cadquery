import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04273, -0.00316).lineTo(0.04991, -0.00316).lineTo(0.04991, -0.01549).lineTo(-0.04273, -0.01549).lineTo(-0.04273, -0.00316).close()
solid=wp_sketch0.add(loop0).extrude(0.10640695226503752)
