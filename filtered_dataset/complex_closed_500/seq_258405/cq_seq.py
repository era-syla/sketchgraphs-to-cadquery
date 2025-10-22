import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.10236, 0.0).lineTo(0.10236, 0.0).lineTo(0.10236, -0.1524).lineTo(-0.10236, -0.1524).lineTo(-0.10236, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.16880550876869474)
